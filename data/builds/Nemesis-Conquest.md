---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.45
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.25
    win_rate: 0.63
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.21
      win_rate: 0.62
    - name: Jotunn's Revenge
      pick_rate: 0.17
      win_rate: 0.3
  - name: The Crusher
    pick_rate: 0.12
    win_rate: 0.76
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.2
      win_rate: 0.46
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.69
  - name: The Reaper
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.63
    - name: Hydra's Lament
      pick_rate: 0.05
      win_rate: 0.43
  - name: Heartseeker
    pick_rate: 0.28
    win_rate: 0.67
    alternates:
    - name: The Reaper
      pick_rate: 0.05
      win_rate: 0.29
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.57
  - name: Skeggox
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.56
    - name: Avatar's Parashu
      pick_rate: 0.07
      win_rate: 0.88
  - name: Blinking Abyss
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Skeggox
      pick_rate: 0.09
      win_rate: 0.43
    - name: Infused Axe
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.48
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.52
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-09-13'
  god_win_rate: 0.5072463768115942
  god_matches_won: 70
  god_matches_played: 138
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-13'
  god_matches_analyzed: 5560
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus, Riptalon, Spear
    of Desolation, Titan''s Bane, Dominance, Obsidian Shard, Deathbringer, Soul Gem,
    Toxic Blade, The Reaper, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The World Stone,
    Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient
    Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.6
      efficiency: 0.47
      win: 0.76
      pick: 0.16
      fit: 0.54
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.67
      pick: 0.47
      fit: 0.64
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.45
      win: 0.88
      pick: 0.15
      fit: 0.44
  community_ordered:
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Hydra's Lament
  - Death Metal
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  - Avatar's Parashu
  flex_slots:
  - Death Metal
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom Orb, Tekko-Kagi,
    Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Silverbranch
    Bow, Dominance, Bracer of The Abyss, Titan''s Bane, Golden Blade, Dreamer''s Idol,
    Transcendence, Deathbringer, The Reaper, Arondight, Gem of Focus, Book of Thoth,
    Polynomicon, Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s Dual Swords,
    Soul Reaver, Rod of Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.49
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.76
      pick: 0.16
      fit: 0.44
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.47
      fit: 0.62
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.61
      efficiency: 0.45
      win: 0.88
      pick: 0.15
      fit: 0.34
  community_ordered:
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Shield of the Phoenix
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Rod of Tahuti, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, Riptalon,
    Runeforged Hammer, The Reaper, Freya''s Tears, Gluttonous Grimoire, Shifter''s
    Shield, Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s Necklace,
    Eye of the Storm, Genji''s Guard, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix
    Feather, Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow,
    Eye of Providence, Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale,
    Avenging Blade, Helm of Radiance, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.69
      pick: 0.12
      fit: 0.42
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.76
      pick: 0.16
      fit: 0.37
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.47
      fit: 0.47
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.45
      win: 0.88
      pick: 0.15
      fit: 0.27
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Berserker's Shield
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  - Avatar's Parashu
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Silverbranch Bow, Tekko-Kagi, Spear of the Magus,
    Death Metal, Spear of Desolation, Obsidian Shard, Titan''s Bane, Soul Gem, Riptalon,
    Gluttonous Grimoire, The Reaper, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb,
    The World Stone, Nimble Ring, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, Transcendence,
    The Executioner, Runeforged Hammer, Arondight, Ancient Signet, Qin''s Blade, Chronos''
    Pendant.'
  slot_scores:
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.68
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.62
      efficiency: 0.47
      win: 0.76
      pick: 0.16
      fit: 0.67
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.67
      pick: 0.47
      fit: 0.77
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.43
    Avatar's Parashu:
      total: 0.65
      efficiency: 0.45
      win: 0.88
      pick: 0.15
      fit: 0.57
  community_ordered:
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    Berserker''s Shield, The Reaper, Spear of the Magus, Toxic Blade, Bragi''s Harp,
    Obsidian Shard, Spear of Desolation, Dominance, Bracer of The Abyss, Qin''s Blade,
    Titan''s Bane, Deathbringer, Demon Blade, Doom Orb, The World Stone, Ancient Signet,
    Sun Beam Bow, Blood-Bound Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant,
    Musashi''s Dual Swords, Runeforged Hammer, Arondight, Bancroft''s Talon, Pendulum
    Blade.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.76
      pick: 0.16
      fit: 0.37
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.47
      fit: 0.47
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.45
      win: 0.88
      pick: 0.15
      fit: 0.27
  community_ordered:
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Avatar's Parashu
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Silverbranch
    Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow, Pendulum
    Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem
    of Death, Doom Orb, Riptalon, Golden Blade, The World Stone, Ancient Signet, Titan''s
    Bane, Breastplate of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer, Dominance,
    The Reaper, Genji''s Guard, Qin''s Blade, Transcendence, Musashi''s Dual Swords,
    Runeforged Hammer, Demon Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.55
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.76
      pick: 0.16
      fit: 0.34
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.24
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.45
      win: 0.88
      pick: 0.15
      fit: 0.24
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - The Crusher
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The
    World Stone, Arondight, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru,
    Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.3
      pick: 0.17
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing,
    Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s
    Harp, Spear of the Magus, Riptalon, Spear of Desolation, Titan''s Bane, Dominance,
    Obsidian Shard, Deathbringer, Soul Gem, The Reaper, Toxic Blade, Demon Blade,
    Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum
    Blade, Transcendence, The World Stone, Arondight, Qin''s Blade, Runeforged Hammer,
    Dreamer''s Idol, Damaru, Rage, Ancient Signet, Chronos'' Pendant, Avenging Blade,
    Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.3
      pick: 0.17
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.67
      pick: 0.47
      fit: 0.64
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  swaps:
  - added: Heartseeker
    removed: Silverbranch Bow
    reason: community 67% win over 39 matches (vs 51% on this god), taking the model's
      weakest slot from Silverbranch Bow
  starter: *id001
---
