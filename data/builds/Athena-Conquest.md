---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.53
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.42
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.65
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.58
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.63
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.53
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.78
    - name: Deathbringer
      pick_rate: 0.05
      win_rate: 0.52
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.63
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.69
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.16
    win_rate: 0.67
  - name: Selflessness
    pick_rate: 0.16
    win_rate: 0.53
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-09'
  god_win_rate: 0.5692934782608695
  god_matches_won: 419
  god_matches_played: 736
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-09'
  god_matches_analyzed: 15881
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Breastplate of Valor, Amanita Charm, Kinetic Cuirass,
    Eye of Providence, Berserker''s Shield, Oni Hunter''s Garb, Gluttonous Grimoire,
    Shield of the Phoenix, Erosion, Draconic Scale, Spectral Armor, Hide of the Nemean
    Lion, Shield Splitter, Stampede, Pharaoh''s Curse, Jotunn''s Revenge, Runeforged
    Hammer, Soul Gem, Leviathan''s Hide, The Crusher, Eye of the Storm, Mantle Of
    Discord, Hydra''s Lament, Stone of Binding, Midgardian Mail, Yogi''s Necklace,
    Helm of Radiance, Shogun''s Ofuda, Magi''s Cloak, Rod of Asclepius, Ancile, Gladiator''s
    Shield, Doublet of Binding, Xibalban Effigy, Void Shield, Hussar''s Wings, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.37
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.61
      pick: 0.23
      fit: 0.68
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Breastplate of Valor, Shield of the Phoenix,
    Kinetic Cuirass, Eye of Providence, Berserker''s Shield, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Phoenix
    Feather, Draconic Scale, Spectral Armor, Hide of the Nemean Lion, Runeforged Hammer,
    Stampede, Pharaoh''s Curse, Jotunn''s Revenge, Lifebinder, Yogi''s Necklace, Leviathan''s
    Hide, Eye of the Storm, Blood-Bound Book, The Crusher, Midgardian Mail, Bancroft''s
    Talon, Shield Splitter, Hydra''s Lament, Glorious Pridwen, Shogun''s Ofuda, The
    Reaper, Ancile, Gladiator''s Shield, Jade Scepter, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.34
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.34
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.54
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.61
      pick: 0.23
      fit: 0.66
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gluttonous Grimoire
  - Shifter's Shield
  - Dwarven Plate
  flex_slots:
  - Breastplate of Valor
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Breastplate of Valor, Amanita
    Charm, Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Berserker''s Shield, Soul
    Gem, Eye of Providence, Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle,
    Spear of the Magus, Void Shield, Avenging Blade, The Cosmic Horror, Void Stone,
    Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Runeforged
    Hammer, Draconic Scale, Pharaoh''s Curse, Hydra''s Lament, Obsidian Shard, Yogi''s
    Necklace, Riptalon, Shield Splitter, The Reaper, Silverbranch Bow, Leviathan''s
    Hide, Helm of Radiance, Midgardian Mail, Rod of Asclepius, Eye of the Storm, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.26
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.23
      fit: 0.48
    Dwarven Plate:
      total: 0.53
      efficiency: 0.35
      win: 0.78
      pick: 0.06
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Breastplate of Valor, Berserker''s Shield, Amanita Charm,
    Gluttonous Grimoire, Kinetic Cuirass, Golden Blade, Eye of Providence, Pharaoh''s
    Curse, Oni Hunter''s Garb, The Crusher, Jotunn''s Revenge, Riptalon, Runeforged
    Hammer, Lernaean Bow, Hydra''s Lament, Soul Gem, Shogun''s Ofuda, Shield of the
    Phoenix, Tyrfing, Spectral Armor, Silverbranch Bow, Yogi''s Necklace, Shield Splitter,
    Erosion, Eye of the Storm, Bracer of The Abyss, Draconic Scale, Dominance, Death
    Metal, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, Avenging Blade,
    Bragi''s Harp, Midgardian Mail, Damaru, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.2
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.33
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Dwarven Plate
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Hydra''s Lament, Soul Gem, Gluttonous Grimoire, Eye of Providence, Oni
    Hunter''s Garb, The Crusher, Chronos'' Pendant, Runeforged Hammer, Screeching
    Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Spectral
    Armor, Erosion, Shield Splitter, Hide of the Nemean Lion, Yogi''s Necklace, Pharaoh''s
    Curse, Prophetic Cloak, Draconic Scale, Helm of Radiance, Rod of Asclepius, Gem
    of Focus, Eye of the Storm, Arondight, Death Metal, Leviathan''s Hide, Jade Scepter,
    Midgardian Mail, Spear of the Magus, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.48
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.23
      fit: 0.45
    Dwarven Plate:
      total: 0.53
      efficiency: 0.35
      win: 0.78
      pick: 0.06
      fit: 0.32
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Dwarven Plate
  flex_slots:
  - Berserker's Shield
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor, Berserker''s
    Shield, The Crusher, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic
    Cuirass, Eye of Providence, Runeforged Hammer, Hydra''s Lament, Oni Hunter''s
    Garb, Shield Splitter, Soul Gem, Golden Blade, Lernaean Bow, Eye of the Storm,
    Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor, Avenging
    Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Spear of the Magus, Draconic
    Scale, Shogun''s Ofuda, Leviathan''s Hide, Dominance, The Cosmic Horror, Helm
    of Radiance, Heartseeker, Rod of Asclepius, Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.23
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.38
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.23
      fit: 0.42
    Dwarven Plate:
      total: 0.52
      efficiency: 0.35
      win: 0.78
      pick: 0.06
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gluttonous Grimoire
  - Shifter's Shield
  - Dwarven Plate
  flex_slots:
  - Gluttonous Grimoire
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Gluttonous Grimoire, Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Berserker''s Shield, Soul Gem, Eye of Providence, Runeforged Hammer, Oni Hunter''s
    Garb, Hydra''s Lament, Death Metal, Spear of the Magus, Shield Splitter, The Cosmic
    Horror, Helm of Radiance, Shield of the Phoenix, Rod of Asclepius, Eye of the
    Storm, Spectral Armor, Erosion, Spear of Desolation, Jade Scepter, Yogi''s Necklace,
    Pharaoh''s Curse, Avenging Blade, Draconic Scale, Golden Blade, Obsidian Shard,
    Lernaean Bow, The Reaper, Triton''s Conch, Chronos'' Pendant, Damaru, Leviathan''s
    Hide, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.23
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.61
      pick: 0.14
      fit: 0.23
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.23
      fit: 0.42
    Dwarven Plate:
      total: 0.52
      efficiency: 0.35
      win: 0.78
      pick: 0.06
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Oni Hunter''s Garb, Gluttonous Grimoire, Shield of the
    Phoenix, Erosion, Breastplate of Valor, Draconic Scale, Spectral Armor, Shield
    Splitter, Pharaoh''s Curse, Jotunn''s Revenge, Runeforged Hammer, Soul Gem, Leviathan''s
    Hide, The Crusher, Eye of the Storm, Mantle Of Discord, Hydra''s Lament, Stone
    of Binding, Midgardian Mail, Yogi''s Necklace, Hide of the Nemean Lion, Helm of
    Radiance, Shogun''s Ofuda, Magi''s Cloak, Stampede, Rod of Asclepius, Ancile,
    Gladiator''s Shield, Doublet of Binding, Xibalban Effigy, Void Shield, Hussar''s
    Wings, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.16
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.05
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
