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
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.57
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.52
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.59
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.72
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.52
    - name: Deathbringer
      pick_rate: 0.08
      win_rate: 0.5
  - name: Deathbringer
    pick_rate: 0.06
    win_rate: 0.66
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.57
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.7
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.45
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.64
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.52
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-19'
  god_win_rate: 0.5684380032206119
  god_matches_won: 353
  god_matches_played: 621
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Rod of Tahuti, Gluttonous Grimoire, Erosion, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Spectral Armor, Hydra''s
    Lament, Shield Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the
    Storm, Nimble Ring, Magi''s Cloak, Runeforged Hammer, Stampede, Ancile, Gladiator''s
    Shield, Shogun''s Ofuda, Screeching Gargoyle, Prophetic Cloak, Helm of Radiance,
    Void Shield, Doublet of Binding, Hussar''s Wings, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.37
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.17
      fit: 0.68
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.57
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Chandra''s Grace, Rod of Tahuti,
    Rod of Asclepius, Oni Hunter''s Garb, Erosion, Eye of Providence, Phoenix Feather,
    Draconic Scale, Breastplate of Valor, Spectral Armor, Jotunn''s Revenge, Pharaoh''s
    Curse, Leviathan''s Hide, The Crusher, Midgardian Mail, Runeforged Hammer, Eye
    of the Storm, Glorious Pridwen, Lifebinder, Nimble Ring, Shield Splitter, Gladiator''s
    Shield, Ancile, Blood-Bound Book, Shogun''s Ofuda, The Reaper, Void Shield, Doublet
    of Binding, Mantle Of Discord, Bancroft''s Talon, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.34
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.54
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Rod of Tahuti, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding,
    Berserker''s Shield, Screeching Gargoyle, Void Shield, The Cosmic Horror, Oni
    Hunter''s Garb, Breastplate of Valor, Hydra''s Lament, Spear of the Magus, Void
    Stone, Shield of the Phoenix, Spear of Desolation, Avenging Blade, Erosion, Eye
    of Providence, Spectral Armor, Nimble Ring, Draconic Scale, Obsidian Shard, The
    Reaper, Pharaoh''s Curse, Riptalon, Shield Splitter, Leviathan''s Hide, Midgardian
    Mail, Runeforged Hammer, Silverbranch Bow, Mantle Of Discord, Eye of the Storm,
    Helm of Radiance, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
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
    this god: Freya''s Tears, Berserker''s Shield, Nimble Ring, Rod of Tahuti, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Hydra''s Lament, Golden Blade, The
    Crusher, Pharaoh''s Curse, Jotunn''s Revenge, Breastplate of Valor, Riptalon,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Shogun''s Ofuda, Tyrfing,
    Runeforged Hammer, Spectral Armor, Erosion, Lernaean Bow, Silverbranch Bow, Shield
    Splitter, Eye of Providence, Draconic Scale, Eye of the Storm, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Toxic Blade, Stone of Binding, Helm of Radiance,
    Death Metal, Screeching Gargoyle, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.47
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.33
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Hydra''s Lament, Breastplate
    of Valor, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Rod of Tahuti,
    Amanita Charm, Soul Gem, Gluttonous Grimoire, Berserker''s Shield, The Crusher,
    Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Prophetic Cloak, Shield Splitter, Draconic Scale, Runeforged Hammer,
    Pharaoh''s Curse, Eye of the Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Totem of Death, Stone of Binding, Arondight,
    Death Metal, Rod of Asclepius, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.55
      pick: 0.14
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Hydra's Lament:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.14
      fit: 0.52
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Hydra''s Lament, Kinetic Cuirass, Berserker''s Shield, Amanita
    Charm, Gluttonous Grimoire, Nimble Ring, Runeforged Hammer, Shield Splitter, Breastplate
    of Valor, Oni Hunter''s Garb, Soul Gem, Golden Blade, Eye of the Storm, Shield
    of the Phoenix, Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence,
    The Reaper, Lernaean Bow, Draconic Scale, Death Metal, Avenging Blade, Damaru,
    The Cosmic Horror, Shogun''s Ofuda, Leviathan''s Hide, Spear of the Magus, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Tekko-Kagi, Spear of Desolation, Helm
    of Radiance, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.62
      pick: 0.14
      fit: 0.4
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.38
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Hydra''s
    Lament, Soul Gem, Berserker''s Shield, Nimble Ring, Breastplate of Valor, Oni
    Hunter''s Garb, The Cosmic Horror, Runeforged Hammer, Shield Splitter, Shield
    of the Phoenix, Death Metal, Spear of the Magus, Erosion, Spear of Desolation,
    Eye of the Storm, Helm of Radiance, Spectral Armor, Eye of Providence, Draconic
    Scale, Rod of Asclepius, Pharaoh''s Curse, The Reaper, Obsidian Shard, Leviathan''s
    Hide, Golden Blade, Chronos'' Pendant, Jade Scepter, Midgardian Mail, Avenging
    Blade, Mantle Of Discord, Damaru, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Berserker's Shield
  - Erosion
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s
    Shield, Rod of Tahuti, Gluttonous Grimoire, Erosion, Shield of the Phoenix, Eye
    of Providence, Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Spectral
    Armor, Shield Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the
    Storm, Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Gladiator''s Shield,
    Shogun''s Ofuda, Screeching Gargoyle, Prophetic Cloak, Helm of Radiance, Void
    Shield, Doublet of Binding, Hydra''s Lament, Hussar''s Wings, Stampede, Chandra''s
    Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.19
      fit: 0.37
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.72
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.68
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.68
  starter: *id001
---
