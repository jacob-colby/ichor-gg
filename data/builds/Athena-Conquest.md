---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.55
  slot_order:
  - name: Stampede
    pick_rate: 0.21
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.5
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Deathbringer
      pick_rate: 0.08
      win_rate: 0.64
  - name: Deathbringer
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.67
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.83
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.51
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.52
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-14'
  god_win_rate: 0.5032258064516129
  god_matches_won: 78
  god_matches_played: 155
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s Shield,
    Hydra''s Lament, Gluttonous Grimoire, Oni Hunter''s Garb, Shield of the Phoenix,
    Erosion, Eye of Providence, Shifter''s Shield, Draconic Scale, Spectral Armor,
    Jotunn''s Revenge, Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, The Crusher, Eye of the
    Storm, Helm of Radiance, Shogun''s Ofuda, Magi''s Cloak, Runeforged Hammer, Ancile,
    Gladiator''s Shield, Xibalban Effigy, Screeching Gargoyle, Hide of the Nemean
    Lion, Void Shield, Prophetic Cloak, Doublet of Binding, Rod of Asclepius, Yogi''s
    Necklace, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.29
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Freya''s Tears, Rod of
    Asclepius, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Eye of Providence, Shifter''s
    Shield, Phoenix Feather, Draconic Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s
    Curse, Leviathan''s Hide, Blood-Bound Book, Bancroft''s Talon, Midgardian Mail,
    Lifebinder, Runeforged Hammer, The Crusher, Eye of the Storm, Glorious Pridwen,
    Shogun''s Ofuda, Shield Splitter, Riptalon, Gladiator''s Shield, Ancile, Yogi''s
    Necklace, Hide of the Nemean Lion, Void Shield, Mantle Of Discord, Stone of Binding,
    Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.34
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.9
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.3
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, Kinetic Cuirass, Hydra''s
    Lament, The Crusher, Soul Gem, Amanita Charm, Freya''s Tears, Berserker''s Shield,
    Stone of Binding, Screeching Gargoyle, Spear of the Magus, Void Shield, Oni Hunter''s
    Garb, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear of Desolation,
    Avenging Blade, Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Shifter''s
    Shield, Riptalon, Pharaoh''s Curse, Draconic Scale, Silverbranch Bow, The Reaper,
    Shield Splitter, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Runeforged Hammer, Shogun''s Ofuda, The World Stone, Doom Orb, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.58
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Hydra's Lament
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Hydra''s Lament, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Freya''s Tears, Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge,
    Riptalon, The Crusher, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda,
    Shield of the Phoenix, Silverbranch Bow, Tyrfing, Runeforged Hammer, Spectral
    Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of The Abyss, Shifter''s
    Shield, Draconic Scale, Helm of Radiance, Eye of the Storm, Leviathan''s Hide,
    Midgardian Mail, Death Metal, Mantle Of Discord, Yogi''s Necklace, Stone of Binding,
    Eros'' Bow, Dominance, Spear of the Magus, Rod of Asclepius, Blood-Bound Book.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.34
    Pharaoh's Curse:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Freya''s Tears, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous
    Grimoire, Berserker''s Shield, Oni Hunter''s Garb, Screeching Gargoyle, Chronos''
    Pendant, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s Shield,
    Erosion, Spectral Armor, Prophetic Cloak, Eye of Providence, Pharaoh''s Curse,
    Shifter''s Shield, Shield Splitter, Draconic Scale, Helm of Radiance, Runeforged
    Hammer, Gem of Focus, Totem of Death, Leviathan''s Hide, Eye of the Storm, Mantle
    Of Discord, Rod of Asclepius, Midgardian Mail, Stone of Binding, Spear of the
    Magus, Death Metal, Arondight, Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.55
    Hydra's Lament:
      total: 0.57
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Freya''s
    Tears, Soul Gem, Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion,
    Spectral Armor, Death Metal, Eye of Providence, Spear of the Magus, Shifter''s
    Shield, Shogun''s Ofuda, Damaru, Draconic Scale, The Reaper, The Cosmic Horror,
    Avenging Blade, Riptalon, Leviathan''s Hide, Helm of Radiance, Midgardian Mail,
    Mantle Of Discord, Stone of Binding, Heartseeker, Silverbranch Bow, Yogi''s Necklace,
    Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.56
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Hydra''s Lament,
    Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s
    Shield, Freya''s Tears, Spear of the Magus, Oni Hunter''s Garb, Death Metal, The
    Cosmic Horror, Runeforged Hammer, Helm of Radiance, Shield Splitter, Shield of
    the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of the Storm, Rod
    of Asclepius, Eye of Providence, Pharaoh''s Curse, Jade Scepter, Obsidian Shard,
    Shifter''s Shield, Draconic Scale, Chronos'' Pendant, Golden Blade, Leviathan''s
    Hide, Blood-Bound Book, Damaru, Lernaean Bow, The Reaper, Bancroft''s Talon, Ethereal
    Staff, Wish-Granting Pearl, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.23
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.55
      efficiency: 0.58
      win: 0.64
      pick: 0.14
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Shield
    of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Spectral Armor, Jotunn''s
    Revenge, Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, The Crusher, Eye of the Storm,
    Helm of Radiance, Shogun''s Ofuda, Magi''s Cloak, Hydra''s Lament, Runeforged
    Hammer, Ancile, Gladiator''s Shield, Xibalban Effigy, Screeching Gargoyle, Hide
    of the Nemean Lion, Void Shield, Prophetic Cloak, Doublet of Binding, Rod of Asclepius,
    Yogi''s Necklace, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.52
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.16
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: *id001
---
