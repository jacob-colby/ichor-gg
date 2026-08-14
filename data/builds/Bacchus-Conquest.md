---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.58
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.23
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.46
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.46
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.54
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.33
    alternates:
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.25
  - name: Kinetic Cuirass
    pick_rate: 0.12
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.05
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.05
      win_rate: 0.4
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.4
  - name: Veve Charm
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.75
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.46
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.63
  - name: Warrior's Axe
    pick_rate: 0.13
    win_rate: 0.2
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-14'
  god_win_rate: 0.48333333333333334
  god_matches_won: 58
  god_matches_played: 120
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Freya''s Tears, Gluttonous Grimoire,
    Oni Hunter''s Garb, Prophetic Cloak, Erosion, Shield of the Phoenix, Eye of Providence,
    Draconic Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s Curse, Shield Splitter,
    Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail,
    The Crusher, Eye of the Storm, Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak,
    Hydra''s Lament, Runeforged Hammer, Ancile, Gladiator''s Shield, Xibalban Effigy,
    Void Shield, Screeching Gargoyle, Doublet of Binding, Rod of Asclepius, Hussar''s
    Wings, Yogi''s Necklace, Hide of the Nemean Lion, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.78
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.48
      pick: 0.25
      fit: 0.68
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
    Stampede:
      total: 0.52
      efficiency: 0.48
      win: 0.62
      pick: 0.19
      fit: 0.44
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Amanita Charm
  - Stampede
  flex_slots:
  - Stampede
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Soul Gem,
    Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s
    Grace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Spectral Armor,
    Jotunn''s Revenge, Pharaoh''s Curse, Leviathan''s Hide, Blood-Bound Book, Bancroft''s
    Talon, Midgardian Mail, Lifebinder, Runeforged Hammer, Eye of the Storm, The Crusher,
    Glorious Pridwen, Shogun''s Ofuda, Shield Splitter, Riptalon, Gladiator''s Shield,
    Hydra''s Lament, Ancile, Void Shield, Mantle Of Discord, The Reaper, Yogi''s Necklace,
    Hide of the Nemean Lion, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.76
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.96
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.62
      pick: 0.19
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Stone of Binding
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
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Soul Gem, Amanita
    Charm, Berserker''s Shield, Stone of Binding, Screeching Gargoyle, Freya''s Tears,
    Spear of the Magus, Void Shield, Oni Hunter''s Garb, The Cosmic Horror, Void Stone,
    Shield of the Phoenix, Spear of Desolation, Avenging Blade, Erosion, Eye of Providence,
    Spectral Armor, Obsidian Shard, Riptalon, Pharaoh''s Curse, Draconic Scale, Silverbranch
    Bow, The Reaper, Shield Splitter, Hydra''s Lament, Leviathan''s Hide, Mantle Of
    Discord, Helm of Radiance, Midgardian Mail, Runeforged Hammer, Shogun''s Ofuda,
    Heartseeker, The World Stone, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.74
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Amanita Charm, Golden Blade,
    Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The Crusher, Freya''s Tears, Oni
    Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Shield of the Phoenix,
    Silverbranch Bow, Hydra''s Lament, Tyrfing, Runeforged Hammer, Spectral Armor,
    Erosion, Shield Splitter, Eye of Providence, Bracer of The Abyss, Draconic Scale,
    Eye of the Storm, Helm of Radiance, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Death Metal, Stone of Binding, Eros'' Bow, Dominance, Spear of the
    Magus, Rod of Asclepius, Yogi''s Necklace, Breastplate of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.37
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Prophetic Cloak
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Shield of the Phoenix, Soul Gem, Prophetic Cloak, Amanita Charm, Gluttonous Grimoire,
    Berserker''s Shield, Hydra''s Lament, Oni Hunter''s Garb, Screeching Gargoyle,
    Chronos'' Pendant, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s
    Shield, Erosion, Spectral Armor, Eye of Providence, Pharaoh''s Curse, Shield Splitter,
    Draconic Scale, Runeforged Hammer, Helm of Radiance, Gem of Focus, Leviathan''s
    Hide, Eye of the Storm, Mantle Of Discord, Midgardian Mail, Rod of Asclepius,
    Stone of Binding, Spear of the Magus, Death Metal, Arondight, Jade Scepter, Shogun''s
    Ofuda, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.55
    Prophetic Cloak:
      total: 0.51
      efficiency: 0.43
      win: 0.58
      pick: 0.14
      fit: 0.64
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Stampede
  flex_slots:
  - The Crusher
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Amanita Charm, Hydra''s Lament, Freya''s Tears, Soul Gem,
    Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Golden
    Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion, Spectral
    Armor, Death Metal, Eye of Providence, Spear of the Magus, Shogun''s Ofuda, The
    Reaper, Draconic Scale, Damaru, Avenging Blade, The Cosmic Horror, Riptalon, Leviathan''s
    Hide, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Stone of Binding,
    Heartseeker, Silverbranch Bow, Tekko-Kagi, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
    Stampede:
      total: 0.5
      efficiency: 0.48
      win: 0.62
      pick: 0.19
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Stampede
  flex_slots:
  - Berserker's Shield
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Freya''s Tears, Spear
    of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, The Cosmic Horror,
    Runeforged Hammer, Shield Splitter, Helm of Radiance, Shield of the Phoenix, Spear
    of Desolation, Erosion, Spectral Armor, Eye of the Storm, Rod of Asclepius, Eye
    of Providence, Pharaoh''s Curse, Obsidian Shard, Jade Scepter, Draconic Scale,
    Chronos'' Pendant, Golden Blade, Leviathan''s Hide, Blood-Bound Book, Lernaean
    Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle Of Discord,
    Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
    Stampede:
      total: 0.5
      efficiency: 0.48
      win: 0.62
      pick: 0.19
      fit: 0.27
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
    Underrated for this god: Amanita Charm, Berserker''s Shield, Freya''s Tears, Gluttonous
    Grimoire, Breastplate of Valor, Oni Hunter''s Garb, Erosion, Shield of the Phoenix,
    Eye of Providence, Draconic Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s
    Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone
    of Binding, Midgardian Mail, The Crusher, Eye of the Storm, Shogun''s Ofuda, Helm
    of Radiance, Magi''s Cloak, Hydra''s Lament, Runeforged Hammer, Ancile, Gladiator''s
    Shield, Xibalban Effigy, Void Shield, Screeching Gargoyle, Hide of the Nemean
    Lion, Prophetic Cloak, Doublet of Binding, Rod of Asclepius, Yogi''s Necklace,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.71
      win: 0.33
      pick: 0.25
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.4
      efficiency: 0.66
      win: 0.25
      pick: 0.11
      fit: 0.37
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.62
      pick: 0.2
      fit: 0.78
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
