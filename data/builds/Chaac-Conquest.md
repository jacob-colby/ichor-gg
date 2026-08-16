---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.46
  aspect_win_rate: 0.44
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.2
    alternates:
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.33
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.33
  - name: Shield of the Phoenix
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.2
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.25
    - name: The Cosmic Horror
      pick_rate: 0.08
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.17
    alternates:
    - name: Oni Hunter's Garb
      pick_rate: 0.09
      win_rate: 0.67
    - name: Totem of Death
      pick_rate: 0.09
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.0
  - name: Engraved Guard
    pick_rate: 0.18
    win_rate: 0.33
    alternates:
    - name: Medallion
      pick_rate: 0.12
      win_rate: 0.0
    - name: Mana Tome
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.31
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.22
  - name: Warrior's Axe
    pick_rate: 0.1
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-16'
  god_win_rate: 0.3333333333333333
  god_matches_won: 13
  god_matches_played: 39
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, The Crusher, Jotunn''s
    Revenge, Berserker''s Shield, Soul Gem, Nimble Ring, Shield of the Phoenix, The
    Cosmic Horror, Shield Splitter, Runeforged Hammer, Erosion, Hydra''s Lament, Spectral
    Armor, Eye of Providence, Spear of the Magus, Eye of the Storm, Death Metal, Draconic
    Scale, Helm of Radiance, Spear of Desolation, Pharaoh''s Curse, Leviathan''s Hide,
    Rod of Asclepius, Midgardian Mail, Golden Blade, The Reaper, Mantle Of Discord,
    Stone of Binding, Jade Scepter, Obsidian Shard, Avenging Blade, Chronos'' Pendant,
    Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.42
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.55
    Oni Hunter's Garb:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.42
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm, Soul
    Gem, Nimble Ring, Berserker''s Shield, Hydra''s Lament, The Cosmic Horror, Shield
    of the Phoenix, Death Metal, Runeforged Hammer, Shield Splitter, Spear of the
    Magus, Spear of Desolation, Helm of Radiance, Eye of the Storm, Spectral Armor,
    Erosion, Rod of Asclepius, Eye of Providence, Chronos'' Pendant, Draconic Scale,
    Golden Blade, Jade Scepter, The Reaper, Pharaoh''s Curse, Obsidian Shard, Damaru,
    Leviathan''s Hide, Avenging Blade, Yogi''s Necklace, Midgardian Mail, Bancroft''s
    Talon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.64
      win: 0.33
      pick: 0.25
      fit: 0.29
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.45
    Oni Hunter's Garb:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.44
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.43
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.45
      efficiency: 0.77
      win: 0.25
      pick: 0.28
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Berserker''s Shield, The Cosmic Horror, Shield of the Phoenix,
    Nimble Ring, Spear of Desolation, Spear of the Magus, Hydra''s Lament, Runeforged
    Hammer, Shield Splitter, Spectral Armor, Erosion, Death Metal, Eye of Providence,
    Helm of Radiance, Eye of the Storm, The Reaper, Obsidian Shard, Chronos'' Pendant,
    Draconic Scale, Pharaoh''s Curse, Rod of Asclepius, Screeching Gargoyle, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Golden Blade, Chandra''s Grace, Jade
    Scepter, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.64
      win: 0.33
      pick: 0.25
      fit: 0.27
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.48
    Oni Hunter's Garb:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Rod of Asclepius, The Reaper,
    Berserker''s Shield, Chandra''s Grace, Nimble Ring, Blood-Bound Book, Runeforged
    Hammer, The Cosmic Horror, Riptalon, Bancroft''s Talon, Lifebinder, Phoenix Feather,
    Hydra''s Lament, Spectral Armor, Eye of the Storm, Spear of the Magus, Death Metal,
    Erosion, Shield Splitter, Spear of Desolation, Eye of Providence, Draconic Scale,
    Helm of Radiance, Golden Blade, Pharaoh''s Curse, Leviathan''s Hide, Avenging
    Blade, Jade Scepter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.53
    Oni Hunter's Garb:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.3
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.48
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.47
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - The Cosmic Horror
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - The Cosmic Horror
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Soul Gem, Kinetic
    Cuirass, Amanita Charm, The Cosmic Horror, Stone of Binding, Berserker''s Shield,
    Avenging Blade, Screeching Gargoyle, Spear of the Magus, Nimble Ring, Void Shield,
    Spear of Desolation, Shield of the Phoenix, Void Stone, Runeforged Hammer, The
    Reaper, Hydra''s Lament, Obsidian Shard, Shield Splitter, Spectral Armor, Erosion,
    Death Metal, Eye of Providence, Eye of the Storm, Helm of Radiance, Draconic Scale,
    Pharaoh''s Curse, Riptalon, Rod of Asclepius, Leviathan''s Hide, Midgardian Mail,
    Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.48
    Oni Hunter's Garb:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.61
    The Cosmic Horror:
      total: 0.42
      efficiency: 0.58
      win: 0.33
      pick: 0.12
      fit: 0.4
    The Crusher:
      total: 0.45
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Berserker''s Shield, Kinetic Cuirass,
    The Crusher, Amanita Charm, Soul Gem, Jotunn''s Revenge, Golden Blade, Riptalon,
    Pharaoh''s Curse, Shield of the Phoenix, The Cosmic Horror, Silverbranch Bow,
    Runeforged Hammer, Spectral Armor, Hydra''s Lament, Shogun''s Ofuda, Spear of
    the Magus, Tyrfing, Lernaean Bow, Erosion, Helm of Radiance, Shield Splitter,
    Death Metal, Eye of Providence, Spear of Desolation, Toxic Blade, Draconic Scale,
    Rod of Asclepius, Leviathan''s Hide, Eye of the Storm, The Reaper, Bracer of The
    Abyss, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.4
      efficiency: 0.53
      win: 0.33
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.43
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.44
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.33
    Oni Hunter's Garb:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.44
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - The Crusher
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Kinetic Cuirass, Amanita Charm, The Crusher,
    Berserker''s Shield, Hydra''s Lament, Spear of Desolation, Nimble Ring, Screeching
    Gargoyle, Chronos'' Pendant, Chandra''s Grace, The Cosmic Horror, Erosion, Gladiator''s
    Shield, Spectral Armor, Eye of Providence, Runeforged Hammer, Prophetic Cloak,
    Shield Splitter, Draconic Scale, Spear of the Magus, Pharaoh''s Curse, Leviathan''s
    Hide, Helm of Radiance, Eye of the Storm, Midgardian Mail, Gem of Focus, Mantle
    Of Discord, Stone of Binding, Death Metal, Arondight.'
  slot_scores:
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.64
      win: 0.33
      pick: 0.25
      fit: 0.43
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.5
    Oni Hunter's Garb:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.15
      fit: 0.26
    The Crusher:
      total: 0.42
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    The Crusher, Jotunn''s Revenge, Berserker''s Shield, Soul Gem, Nimble Ring, Shield
    of the Phoenix, Shield Splitter, Runeforged Hammer, The Cosmic Horror, Erosion,
    Hydra''s Lament, Spectral Armor, Eye of Providence, Spear of the Magus, Eye of
    the Storm, Death Metal, Draconic Scale, Helm of Radiance, Spear of Desolation,
    Pharaoh''s Curse, Leviathan''s Hide, Rod of Asclepius, Midgardian Mail, Golden
    Blade, The Reaper, Mantle Of Discord, Stone of Binding, Jade Scepter, Obsidian
    Shard, Avenging Blade, Chronos'' Pendant, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.37
      efficiency: 0.69
      win: 0.17
      pick: 0.28
      fit: 0.24
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.77
      win: 0.25
      pick: 0.28
      fit: 0.3
  starter: *id001
---
