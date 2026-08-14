---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.6
  slot_order:
  - name: Transcendence
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.33
    - name: Eye of the Storm
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 1.0
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.0
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Mystical Mail
      pick_rate: 0.11
      win_rate: 0.0
  - name: Totem of Death
    pick_rate: 0.19
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.0
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.0
  - name: Mote of Chaos
    pick_rate: 0.13
    win_rate: 0.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 1.0
  - name: Engraved Guard
    pick_rate: 0.25
    win_rate: 0.5
    alternates:
    - name: Mana Tome
      pick_rate: 0.13
      win_rate: 1.0
    - name: Helm of Radiance
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.35
    win_rate: 0.71
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.29
  - name: Conduit Gem
    pick_rate: 0.1
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-14'
  god_win_rate: 0.45
  god_matches_won: 9
  god_matches_played: 20
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  flex_slots:
  - Gluttonous Grimoire
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Eye of the Storm, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, The Crusher, Berserker''s Shield, Soul Gem, Freya''s Tears, Oni
    Hunter''s Garb, Spear of the Magus, Hydra''s Lament, Shield of the Phoenix, Shield
    Splitter, Runeforged Hammer, Death Metal, The Cosmic Horror, Erosion, Spectral
    Armor, Eye of Providence, Pharaoh''s Curse, Spear of Desolation, Draconic Scale,
    Rod of Asclepius, Jade Scepter, Obsidian Shard, Leviathan''s Hide, Golden Blade,
    Mantle Of Discord, Midgardian Mail, Stone of Binding, Chronos'' Pendant, The Reaper,
    Lernaean Bow, Damaru, Shogun''s Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.55
    Eye of the Storm:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.46
    Helm of Radiance:
      total: 0.72
      efficiency: 0.58
      win: 1.0
      pick: 0.4
      fit: 0.31
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.13
      fit: 0.42
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Eye of the Storm, Gluttonous Grimoire, Soul Gem, The Crusher,
    Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Freya''s Tears, Spear of
    the Magus, Hydra''s Lament, Oni Hunter''s Garb, Shield of the Phoenix, The Cosmic
    Horror, Spear of Desolation, Runeforged Hammer, Death Metal, Shield Splitter,
    Obsidian Shard, Spectral Armor, Erosion, Pharaoh''s Curse, Chronos'' Pendant,
    Eye of Providence, Rod of Asclepius, The Reaper, Draconic Scale, Jade Scepter,
    Leviathan''s Hide, Screeching Gargoyle, Riptalon, Golden Blade, Midgardian Mail,
    Mantle Of Discord, Stone of Binding, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.48
    Eye of the Storm:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.38
    Helm of Radiance:
      total: 0.71
      efficiency: 0.58
      win: 1.0
      pick: 0.4
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.13
      fit: 0.44
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.28
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Heartseeker
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Eye of the Storm
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Eye of the Storm, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, The Crusher,
    Berserker''s Shield, The Reaper, Blood-Bound Book, Bancroft''s Talon, Chandra''s
    Grace, Riptalon, Oni Hunter''s Garb, Runeforged Hammer, Freya''s Tears, Spear
    of the Magus, Hydra''s Lament, Lifebinder, Death Metal, The Cosmic Horror, Phoenix
    Feather, Spectral Armor, Shield Splitter, Erosion, Pharaoh''s Curse, Spear of
    Desolation, Eye of Providence, Jade Scepter, Golden Blade, Draconic Scale, Obsidian
    Shard, Leviathan''s Hide, Sphere of Negation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.42
    Eye of the Storm:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.47
    Helm of Radiance:
      total: 0.72
      efficiency: 0.58
      win: 1.0
      pick: 0.4
      fit: 0.29
    Heartseeker:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.13
      fit: 0.43
    Amanita Charm:
      total: 0.48
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.47
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Eye of the Storm
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Heartseeker, Gluttonous Grimoire, Eye of the
    Storm, The Crusher, Soul Gem, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Spear of the Magus, Stone of Binding, Avenging Blade, The Cosmic Horror, Screeching
    Gargoyle, Void Shield, Freya''s Tears, Oni Hunter''s Garb, Spear of Desolation,
    Obsidian Shard, Hydra''s Lament, Void Stone, Shield of the Phoenix, Runeforged
    Hammer, The Reaper, Death Metal, Shield Splitter, Spectral Armor, Erosion, Riptalon,
    Pharaoh''s Curse, Eye of Providence, Rod of Asclepius, The World Stone, Doom Orb,
    Draconic Scale, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.49
    Eye of the Storm:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.39
    Helm of Radiance:
      total: 0.71
      efficiency: 0.58
      win: 1.0
      pick: 0.4
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.13
      fit: 0.52
    Rod of Tahuti:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.28
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Helm of Radiance
  - Riptalon
  - Heartseeker
  flex_slots:
  - Riptalon
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s Shield, Soul Gem,
    Kinetic Cuirass, Amanita Charm, The Crusher, Riptalon, Golden Blade, Pharaoh''s
    Curse, Oni Hunter''s Garb, Freya''s Tears, Silverbranch Bow, Spear of the Magus,
    Lernaean Bow, Hydra''s Lament, Shogun''s Ofuda, Bracer of The Abyss, Shield of
    the Phoenix, The Cosmic Horror, Runeforged Hammer, Spectral Armor, Death Metal,
    Tyrfing, Erosion, Blood-Bound Book, Rod of Asclepius, Shield Splitter, Bancroft''s
    Talon, Eye of Providence, Spear of Desolation, Jade Scepter, Bragi''s Harp, Obsidian
    Shard, Leviathan''s Hide, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.41
      efficiency: 0.54
      win: 0.33
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.44
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.25
    Helm of Radiance:
      total: 0.7
      efficiency: 0.58
      win: 1.0
      pick: 0.4
      fit: 0.22
    Riptalon:
      total: 0.41
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.13
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Eye of the Storm,
    Soul Gem, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Amanita Charm,
    Shield of the Phoenix, Berserker''s Shield, Hydra''s Lament, The Crusher, Spear
    of Desolation, Oni Hunter''s Garb, Chronos'' Pendant, Screeching Gargoyle, Spear
    of the Magus, Chandra''s Grace, Spectral Armor, Erosion, Gladiator''s Shield,
    Pharaoh''s Curse, Eye of Providence, The Cosmic Horror, Runeforged Hammer, Shield
    Splitter, Prophetic Cloak, Draconic Scale, Gem of Focus, Leviathan''s Hide, Rod
    of Asclepius, Death Metal, Midgardian Mail, Mantle Of Discord, Stone of Binding,
    Yogi''s Necklace, Jade Scepter.'
  slot_scores:
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.66
      win: 0.33
      pick: 0.26
      fit: 0.43
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.51
    Eye of the Storm:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.35
    Helm of Radiance:
      total: 0.71
      efficiency: 0.58
      win: 1.0
      pick: 0.4
      fit: 0.23
    Heartseeker:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.13
      fit: 0.32
    Soul Gem:
      total: 0.45
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, Kinetic Cuirass,
    Amanita Charm, The Crusher, Berserker''s Shield, Soul Gem, Freya''s Tears, Oni
    Hunter''s Garb, Spear of the Magus, Hydra''s Lament, Shield of the Phoenix, Shield
    Splitter, Runeforged Hammer, Death Metal, The Cosmic Horror, Erosion, Spectral
    Armor, Eye of Providence, Eye of the Storm, Pharaoh''s Curse, Spear of Desolation,
    Draconic Scale, Rod of Asclepius, Jade Scepter, Obsidian Shard, Leviathan''s Hide,
    Golden Blade, Mantle Of Discord, Midgardian Mail, Stone of Binding, Chronos''
    Pendant, The Reaper, Lernaean Bow, Damaru, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.3
      efficiency: 0.71
      win: 0.0
      pick: 0.22
      fit: 0.24
    Berserker's Shield:
      total: 0.43
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.43
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.42
  starter: *id001
---
